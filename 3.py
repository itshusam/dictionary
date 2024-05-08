service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def open_ticket(service_tickets, ticket_number, customer_name, issue):
    if ticket_number not in service_tickets:
        service_tickets[ticket_number] = {"Customer": customer_name, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_number} has been opened for {customer_name}.")
    else:
        print(f"Ticket {ticket_number} already exists.")

def update_ticket_status(service_tickets, ticket_number, new_status):
    if ticket_number in service_tickets:
        service_tickets[ticket_number]["Status"] = new_status
        print(f"Status of ticket {ticket_number} has been updated to {new_status}.")
    else:
        print(f"Ticket {ticket_number} does not exist.")

def display_tickets(service_tickets, status=None):
    print("Service Tickets:")
    if status:
        print(f"Tickets with status '{status}':")
        for ticket_number, ticket_info in service_tickets.items():
            if ticket_info["Status"] == status:
                print(f"Ticket Number: {ticket_number}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
    else:
        print("All Tickets:")
        for ticket_number, ticket_info in service_tickets.items():
            print(f"Ticket Number: {ticket_number}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
