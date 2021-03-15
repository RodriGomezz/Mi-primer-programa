import pickle
from time import sleep
from tkinter import *
from tkinter import ttk

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=row)
    ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=3, row=row)


def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "),input("Telefono: "), input("Email: "))
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    pass


def find_contact(contacts, name, frame_contact_list):
    search_term = name
    found_contacts = []

    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        for i in contact_indexes:
            cols, row = frame_contact_list.grid_size()
            ttk.Label(frame_contact_list, text=found_contacts[i]["name"]).grid(column=1, row=row)
            ttk.Label(frame_contact_list, text=found_contacts[i]["email"]).grid(column=2, row=row)
            ttk.Label(frame_contact_list, text=found_contacts[i]["phone"]).grid(column=3, row=row)
    elif len(contact_indexes) == 0:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text="No se ha encontrado ninguno.").grid(column=2, row=row)
        return
    else:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=found_contacts[0]["name"]).grid(column=1, row=row)
        ttk.Label(frame_contact_list, text=found_contacts[0]["email"]).grid(column=2, row=row)
        ttk.Label(frame_contact_list, text=found_contacts[0]["phone"]).grid(column=3, row=row)

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    return found_contacts
    sleep(2)


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="50 12 50 12")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="50 12 50 12")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1, sticky=W)

    ttk.Entry(frame_add_contact, width=15, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=phone).grid(column=3, row=2)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=1, sticky=E)

    for child in frame_add_contact.winfo_children():
        child.grid_configure(padx=10)
    for child in frame_contact_list.winfo_children():
        child.grid_configure(padx=30)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
                ).grid(column=3, row=3)

    ttk.Button(frame_add_contact,
               text="Buscar",
               command=lambda: find_contact(contacts, name.get(),frame_contact_list)
               ).grid(column=2, row=3)

    root.mainloop()
    save_contacts(contacts)

if __name__ == "__main__":
    main()