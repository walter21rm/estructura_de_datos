#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctime>
#include <iomanip>
#include <cstdio> // Para eliminar archivos

// Clase para representar a un cliente que reserva una cancha
class Cliente {
private:
    std::string nombre;
    int tiempo; // en minutos
    std::string telefono; // número telefónico
    std::string diaReserva; // día de reserva
    std::string horaReserva; // hora de reserva
    std::string horaFinReserva; // hora de finalización de la reserva
public:
    // Constructor de la clase Cliente
    Cliente(const std::string& nombre, int tiempo, const std::string& telefono, const std::string& diaReserva, const std::string& horaReserva, const std::string& horaFinReserva) : nombre(nombre), tiempo(tiempo), telefono(telefono), diaReserva(diaReserva), horaReserva(horaReserva), horaFinReserva(horaFinReserva) {}

    // Métodos para obtener los atributos del cliente
    std::string getNombre() const {
        return nombre;
    }

    int getTiempo() const {
        return tiempo;
    }

    std::string getTelefono() const {
        return telefono;
    }

    std::string getDiaReserva() const {
        return diaReserva;
    }

    std::string getHoraReserva() const {
        return horaReserva;
    }

    std::string getHoraFinReserva() const {
        return horaFinReserva;
    }
};

// Clase principal para gestionar el alquiler de canchas
class AlquilerCanchas {
private:
    std::vector<Cliente> clientes; // Almacena la información de los clientes

public:
    // Método para registrar un nuevo cliente
    void registrarCliente() {
        std::string nombre;
        int tiempo;
        std::string telefono;
        std::string diaReserva;
        std::string horaReserva;

        // Solicitar información al usuario
        std::cout << "Ingrese el nombre del cliente: ";
        std::cin >> nombre;

        std::cout << "Ingrese el número telefónico del cliente: ";
        std::cin >> telefono;

        std::cout << "Ingrese el día de reserva (ejemplo: Lunes): ";
        std::cin >> diaReserva;

        std::cout << "Ingrese la hora de reserva (ejemplo: 14:30): ";
        std::cin >> horaReserva;

        std::cout << "Ingrese el tiempo de alquiler (en minutos): ";
        std::cin >> tiempo;

        // Calcular la hora de finalización de la reserva
        std::string horaFinReserva = calcularHoraFin(horaReserva, tiempo);

        // Agregar el cliente a la lista de clientes
        clientes.push_back(Cliente(nombre, tiempo, telefono, diaReserva, horaReserva, horaFinReserva));

        std::cout << "Cliente registrado con éxito." << std::endl;

        // Guardar registro en el archivo
        guardarRegistro(nombre, tiempo, telefono, diaReserva, horaReserva, horaFinReserva);
    }

    // Método para eliminar un cliente
    void eliminarCliente() {
        if (clientes.empty()) {
            std::cout << "No hay clientes registrados." << std::endl;
            return;
        }

        std::string nombre;
        std::cout << "Ingrese el nombre del cliente a eliminar: ";
        std::cin >> nombre;

        // Buscar al cliente en la lista y eliminarlo
        for (auto it = clientes.begin(); it != clientes.end(); ++it) {
            if (it->getNombre() == nombre) {
                // Eliminar el archivo de registro asociado al cliente
                std::string rutaArchivo = "C:\\Users\\walte\\OneDrive\\Documentos\\canchas\\" + nombre + "_registro.txt";
                std::remove(rutaArchivo.c_str());

                clientes.erase(it);
                std::cout << "Cliente eliminado con éxito." << std::endl;
                return;
            }
        }

        std::cout << "Cliente no encontrado." << std::endl;
    }

    // Método para mostrar la lista de clientes con sus detalles
    void mostrarClientes() const {
        if (clientes.empty()) {
            std::cout << "No hay clientes registrados." << std::endl;
            return;
        }

        std::cout << "Lista de clientes:" << std::endl;
        for (const auto& cliente : clientes) {
            double costo = calcularCosto(cliente.getTiempo());

            // Mostrar los detalles del cliente y la reserva
            std::cout << "==================================" << std::endl;
            std::cout << "           VOUCHER                " << std::endl;
            std::cout << "==================================" << std::endl;
            std::cout << "Cliente: " << cliente.getNombre() << std::endl;
            std::cout << "Teléfono: " << cliente.getTelefono() << std::endl;
            std::cout << "Día de Reserva: " << cliente.getDiaReserva() << std::endl;
            std::cout << "Hora de Reserva: " << cliente.getHoraReserva() << std::endl;
            std::cout << "Hora de Finalización: " << cliente.getHoraFinReserva() << std::endl;
            std::cout << "Duración: " << cliente.getTiempo() << " minutos" << std::endl;
            std::cout << "Costo: " << costo << " soles" << std::endl;
        }
    }

    // Método para calcular el costo del alquiler en soles
    double calcularCosto(int tiempo) const {
        const double costoPorHora = 50.0;
        return (tiempo / 60.0) * costoPorHora;
    }

    // Método para calcular la hora de finalización de la reserva
    std::string calcularHoraFin(const std::string& horaInicio, int tiempo) const {
        int horas = tiempo / 60;
        int minutos = tiempo % 60;

        int hora = std::stoi(horaInicio.substr(0, 2));
        int minuto = std::stoi(horaInicio.substr(3, 2));

        minuto += minutos;
        hora += horas;

        if (minuto >= 60) {
            hora += 1;
            minuto -= 60;
        }

        std::ostringstream horaFin;
        horaFin << std::setfill('0') << std::setw(2) << hora << ":" << std::setfill('0') << std::setw(2) << minuto;

        return horaFin.str();
    }

    // Método para guardar el registro de reserva en un archivo de texto
    void guardarRegistro(const std::string& nombre, int tiempo, const std::string& telefono, const std::string& diaReserva, const std::string& horaReserva, const std::string& horaFinReserva) {
        // Ruta del archivo de registro
        std::string ruta = "C:\\Users\\walte\\OneDrive\\Documentos\\canchas\\" + nombre + "_registro.txt";

        // Abre el archivo para agregar datos
        std::ofstream archivo(ruta, std::ios::app);

        if (!archivo.is_open()) {
            std::cerr << "Error al abrir el archivo de registro." << std::endl;
            return;
        }

        // Obtiene la fecha y hora actual
        time_t now = time(0);
        tm* tiempoLocal = localtime(&now);
        std::string fechaHora = asctime(tiempoLocal);

        // Escribe el registro en el archivo
        archivo << "==================================" << std::endl;
        archivo << "           NUEVO REGISTRO         " << std::endl;
        archivo << "==================================" << std::endl;
        archivo << "Fecha y Hora: " << fechaHora;
        archivo << "Cliente: " << nombre << std::endl;
        archivo << "Teléfono: " << telefono << std::endl;
        archivo << "Día de Reserva: " << diaReserva << std::endl;
        archivo << "Hora de Reserva: " << horaReserva << std::endl;
        archivo << "Hora de Finalización: " << horaFinReserva << std::endl;
        archivo << "Duración: " << tiempo << " minutos" << std::endl;

        // Cierra el archivo
        archivo.close();
    }
};

// Función principal
int main() {
    AlquilerCanchas alquiler;

    int opcion;
    do {
        // Menú de opciones
        std::cout << "Menú:" << std::endl;
        std::cout << "1. Registrar cliente" << std::endl;
        std::cout << "2. Eliminar cliente" << std::endl;
        std::cout << "3. Mostrar lista de clientes" << std::endl;
        std::cout << "4. Salir" << std::endl;
        std::cout << "Costo por hora de alquiler: 50 soles" << std::endl;
        std::cout << "Ingrese una opción: ";
        std::cin >> opcion;

        // Control de opciones
        switch (opcion) {
            case 1:
                alquiler.registrarCliente();
                break;
            case 2:
                alquiler.eliminarCliente();
                break;
            case 3:
                alquiler.mostrarClientes();
                break;
            case 4:
                std::cout << "Saliendo del programa." << std::endl;
                break;
            default:
                std::cout << "Opción inválida." << std::endl;
        }
    } while (opcion != 4);

    return 0;
}
