class Vault:
    def __init__(self, inventory_list):
        self.inventory = inventory_list


class Heist:
    def __init__(self, vault, duffel_cap):
        self.vault = vault
        self.duffel_cap = duffel_cap

        self.steal()

    def steal(self):
        
