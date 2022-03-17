#STRATERGY PATTERN:

import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    #helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
 

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStratergy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOOrderingStratergy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy #return reversed list

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy
    
class BlackHOleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return[]



class CustomerSupport:
    
    def __init__(self, processing_stratergy: TicketOrderingStrategy):
        self.tickets =[]
        self.processing_stratergy = processing_stratergy
    

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_stratergy: TicketOrderingStrategy): #fifo - first in first out
        # create the ordered list
        ticket_list = processing_stratergy.create_ordering(self.tickets)

        #if its empty, dont do anything
        if len(self.tickets)==0:
            print("There aee no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

        #above code removed below codes:
        """
        if processing_stratergy == 'fifo':
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_stratergy == 'filo':
            for ticket in reversed(self.tickets): - reversed the tickets
                self.process_ticket(ticket)
        elif processing_stratergy == 'random':
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)"""

    def process_ticket(self, ticket: SupportTicket):
        print("===================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue:{ticket.issue}")
        print("===================================")


    #create the application
app = CustomerSupport(RandomOrderingStrategy())

#Register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastion", "I cant upload any videos, pls help")
app.create_ticket("Arjan Egges" , "VScode doesnt automatically solve my bugs")

# process the tickets 
app.process_tickets(RandomOrderingStrategy())


