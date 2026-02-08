################################################################################
from helpers import generate_id
from guest import Guest
################################################################################
class Hotel:
    ranking_weights = {
        "Resort": { "night_weight": 5, "spent_divider": 5 },
        "Hotel": { "night_weight": 25, "spent_divider": 50 },
        "Boutique": { "night_weight": 15, "spent_divider": 15 },
        "Economy": { "night_weight": 50, "spent_divider": 100 }
    }
    cheapest_cost_per_night = {
        "Resort": 250,
        "Hotel": 125,
        "Boutique": 75,
        "Economy": 50
    }
    def __init__(self, name, location, rooms, capacity, property_type):
        self.id = generate_id()
        self.name = name
        self.location = location
        self.rooms = rooms
        self.capacity = capacity
        self.property_type = property_type
        self.guests = {}

    def add_guest_details(self, guest, nights=1, spent=0.0):
        if not isinstance(guest, Guest):
            print(f"this is not a guest")
        elif guest.id in self.guests.keys():
            print(f"{guest.get_full_name()} is already in this hotel")
        else:
            min_spent = Hotel.cheapest_cost_per_night[self.property_type]
            guest_details = {
                "guest": guest,
                "nights": nights,
                "spent": spent if spent else min_spent,
                "score": 0,
                "tier": "Bronze",
                "checked_status": True
            }
            self.guests[guest.id] = guest_details
            self.calculate_guests_score()
            self.calculate_guests_tier()

    def update_guest_details(self, guest_id, nights, spent):
        if guest_id in self.guests.keys():
            self.guests[guest_id]["nights"] += nights
            self.guests[guest_id]["spent"] += spent
            self.calculate_guests_score()
            self.calculate_guests_tier()
        else:
            print(f"{guest_id} is not in this hotel")

    def check_out_guest(self, guest_id):
        if guest_id in self.guests.keys():
            self.guests[guest_id]["checked_status"] = False

    def check_in_guest(self, guest_id):
        if guest_id in self.guests.keys():
            self.guests[guest_id]["checked_status"] = True

    def calculate_guests_score(self):
        for guest_info in self.guests.values():
            hotel_type = Hotel.ranking_weights[self.property_type]
            score = guest_info["nights"] * hotel_type["night_weight"] + guest_info["spent"] / hotel_type["spent_divider"]
            guest_info["score"] = round(float(score), 2)

    def calculate_guests_tier(self):
        for guest_info in self.guests.values():
            if guest_info["score"] < 100:
                guest_info["tier"] = "Bronze"
            elif guest_info["score"] < 250:
                guest_info["tier"] = "Silver"
            elif guest_info["score"] < 500:
                guest_info["tier"] = "Gold"
            else:
                guest_info["tier"] = "Platinum"

    def get_average_guests_age(self):
        if not self.guests:
            return "There is no guest in this hotel"
        all_guests_age = [guest_details.get("guest").age for guest_details in self.guests.values()]
        return round(sum(all_guests_age) / len(self.guests), 2)
    def get_average_guests_spent(self):
        if not self.guests:
            return "There is no guest in this hotel"
        all_guests_spent = [guest_details.get("spent") for guest_details in self.guests.values()]
        return round(sum(all_guests_spent) / len(self.guests), 2)
    def get_average_guests_nights(self):
        if not self.guests:
            return "There is no guest in this hotel"
        all_guests_nights = [guest_details.get("nights") for guest_details in self.guests.values()]
        return round(sum(all_guests_nights) / len(self.guests), 2)
    def get_average_guests_score(self):
        if not self.guests:
            return "There is no guest in this hotel"
        all_guests_score = [guest_details.get("score") for guest_details in self.guests.values()]
        return round(sum(all_guests_score) / len(self.guests), 2)

    def get_guest_info(self, guest_id):
        if guest_id in self:
            guest_details = self.guests[guest_id]
            guest = guest_details.get("guest")
            return f"{guest.get_full_name()} is {guest.gender}, {guest.age} years old, stayed {guest_details.get('nights')} nights, spent ${guest_details.get('spent')}, score {guest_details.get('score')} points, obtained {guest_details.get('tier')} tier and he is {'checked in' if guest_details.get('checked_status') else 'checked out'}"
        return f"{guest_id} is not checked in this hotel"

    def get_guests_by_tier(self, tier):
        tier_guest_list = [guest_details for guest_details in self.guests.values() if guest_details.get("tier") == tier]
        return tier_guest_list if tier_guest_list else "There is no guest with this tier in this hotel"

    def get_guests_by_rank(self, rank):
        rank_guest_list = [guest_details for guest_details in self.guests.values() if guest_details.get("score") == rank]
        return rank_guest_list if rank_guest_list else "There is no guest with this rank in this hotel"

    def get_checked_in_guests(self):
        checked_in_guests = [guest_details for guest_details in self.guests.values() if guest_details.get("checked_status")]
        return checked_in_guests if checked_in_guests else "There is no checked in guest in this hotel"

    def get_checked_out_guests(self):
        checked_out_guests = [guest_details for guest_details in self.guests.values() if not guest_details.get("checked_status")]
        return checked_out_guests if checked_out_guests else "There is no checked out guest in this hotel"

    def get_all_guests(self):
        all_guests = [guest_details for guest_details in self.guests.values()]
        return all_guests if all_guests else "There is no guest in this hotel"

    def get_sorted_guests_info(self):
        if not self.guests:
            return "There is no guest in this hotel"
        all_guests_details = sorted(self.guests.values(), key=lambda guest_info: guest_info["score"], reverse=True)
        return [self.get_guest_info(guest_details.get("guest").id) for guest_details in all_guests_details]

    def get_all_guests_info(self):
        if not self.guests:
            return "There is no guest in this hotel"
        return [self.get_guest_info(guest_id) for guest_id in self.guests.keys()]

    def get_all_guests_info_by_tier(self, tier):
        all_guests_info = [self.get_guest_info(guest_id) for guest_id in self.guests.keys() if self.guests[guest_id].get("tier") == tier]
        return all_guests_info if all_guests_info else "There is no guest with this tier in this hotel"

    def get_all_guests_info_by_rank(self, rank):
        all_guests_info = [self.get_guest_info(guest_id) for guest_id in self.guests.keys() if self.guests[guest_id].get("score") == rank]
        return all_guests_info if all_guests_info else "There is no guest with this rank in this hotel"

    def __str__(self):
        return f"""Hotel Details:
    ----------------
    ID: {self.id}
    Name: {self.name}
    Location: {self.location}
    Property Type: {self.property_type}
    Guests Count: {len(self)}
    ----------------"""
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.guests)

    def __getitem__(self, guest_id):
        return self.get_guest_info(guest_id)
    def __setitem__(self, guest_id, guest_details):
        if guest_id in self.guests.keys():
            self.update_guest_details(guest_id, guest_details.get("nights"), guest_details.get("spent"))
        else:
            print(f"guest with id {guest_id} not found to update his details")
    def __delitem__(self, guest_id):
        del self.guests[guest_id]

    def __contains__(self, guest_id):
        return guest_id in self.guests
    def __iter__(self):
        return iter(self.guests)
    def __reversed__(self):
        return reversed(self.guests)
