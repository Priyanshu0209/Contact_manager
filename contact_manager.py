import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")
        self.root.config(bg="lightgray")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Manager", font=("Helvetica", 24, "bold"), bg="lightgray")
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", font=("Helvetica", 14), command=self.add_contact)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(self.root, text="Search Contact", font=("Helvetica", 14), command=self.search_contact)
        self.search_button.pack(pady=10)

        self.view_button = tk.Button(self.root, text="View All Contacts", font=("Helvetica", 14), command=self.view_contacts)
        self.view_button.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.root, font=("Helvetica", 14), width=50, height=10)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind('<Double-1>', self.show_contact_details)

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Phone", "Enter contact phone number:")
            email = simpledialog.askstring("Email", "Enter contact email:")
            address = simpledialog.askstring("Address", "Enter contact address:")
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully")
            self.view_contacts()

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if query:
            result = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
            self.contact_listbox.delete(0, tk.END)
            for contact in result:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def show_contact_details(self, event):
        selection = self.contact_listbox.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            detail_message = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
            detail_window = tk.Toplevel(self.root)
            detail_window.title("Contact Details")
            detail_window.geometry("300x200")
            detail_window.config(bg="lightgray")
            tk.Label(detail_window, text=detail_message, font=("Helvetica", 14), bg="lightgray").pack(pady=20)
            tk.Button(detail_window, text="Update", font=("Helvetica", 12), command=lambda: self.update_contact(index, detail_window)).pack(pady=5)
            tk.Button(detail_window, text="Delete", font=("Helvetica", 12), command=lambda: self.delete_contact(index, detail_window)).pack(pady=5)

    def update_contact(self, index, window):
        name = simpledialog.askstring("Name", "Enter new contact name:", initialvalue=self.contacts[index]['name'])
        if name:
            phone = simpledialog.askstring("Phone", "Enter new contact phone number:", initialvalue=self.contacts[index]['phone'])
            email = simpledialog.askstring("Email", "Enter new contact email:", initialvalue=self.contacts[index]['email'])
            address = simpledialog.askstring("Address", "Enter new contact address:", initialvalue=self.contacts[index]['address'])
            self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully")
            window.destroy()
            self.view_contacts()

    def delete_contact(self, index, window):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?"):
            del self.contacts[index]
            messagebox.showinfo("Success", "Contact deleted successfully")
            window.destroy()
            self.view_contacts()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
