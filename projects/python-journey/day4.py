contacts = {}
groups = set()
call_history = []
location = ("Chicago", "US", "60601")

def add_contact(name,phone,email):
    contacts[name] = {"phone": phone,"email": email}
    print(f"Contact {name} added!")

def find_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]['phone'] } and {contacts[name]['email']}")
    else:
        print("not found")

def del_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print(f'No contact found')
def show_all():
    if not contacts :
        print(f'No contacts found')
    
    else:
        for name, info in contacts.items():
            print(f"{name}: {info['phone']} | {info['email']}")



    

if __name__ == "__main__":
    
    # Add contacts
    add_contact("Bob", "555-5678", "bob@gmail.com")
    add_contact("Alvar", "555-1234", "alvar@gmail.com")
    add_contact("Diana", "555-9999", "diana@gmail.com")
    
    # Show all
    show_all()
    
    # Find someone
    find_contact("Bob")
    find_contact("Zara")    # not found!
    
    # Delete someone
    del_contact("Bob")
    
    # Show all again — Bob should be gone
    show_all()
    

