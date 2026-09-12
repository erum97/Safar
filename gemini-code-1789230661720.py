# sample_data.py
SAMPLE_TRIP_DATA = {
    "traveler_name": "Alex",
    "country": "United Kingdom",
    "number_of_travelers": 2,
    "budget": 2500,
    "currency": "USD",
    "duration_days": 7,
    "cities": [
        "Lahore",
        "Islamabad",
        "Hunza",
    ],
    "hotels": [
        {
            "city": "Lahore",
            "name": "Sample Hotel Lahore",
            "address": "Gulberg, Lahore",
        },
        {
            "city": "Islamabad",
            "name": "Sample Hotel Islamabad",
            "address": "F-7, Islamabad",
        },
        {
            "city": "Hunza",
            "name": "Sample Hotel Hunza",
            "address": "Karimabad, Hunza",
        },
    ],
    "itinerary": [
        {
            "day": 1,
            "city": "Lahore",
            "activities": [
                "Arrive in Lahore",
                "Visit Lahore Fort",
                "Explore the Walled City",
            ],
        },
        {
            "day": 2,
            "city": "Lahore",
            "activities": [
                "Visit Badshahi Mosque",
                "Try local Pakistani food",
                "Visit Minar-e-Pakistan",
            ],
        },
        {
            "day": 3,
            "city": "Islamabad",
            "activities": [
                "Travel from Lahore to Islamabad",
                "Visit Faisal Mosque",
                "Explore Daman-e-Koh",
            ],
        },
        {
            "day": 4,
            "city": "Islamabad",
            "activities": [
                "Visit Pakistan Monument",
                "Explore Lok Virsa Museum",
            ],
        },
        {
            "day": 5,
            "city": "Hunza",
            "activities": [
                "Travel to Hunza",
                "Explore Karimabad",
                "Visit Baltit Fort",
            ],
        },
        {
            "day": 6,
            "city": "Hunza",
            "activities": [
                "Visit Attabad Lake",
                "Explore Passu Cones",
                "Cross Hussaini Suspension Bridge",
            ],
        },
        {
            "day": 7,
            "city": "Islamabad / Departure",
            "activities": [
                "Return to Islamabad",
                "Shopping for souvenirs at Centaurus Mall",
                "Departure",
            ],
        },
    ],
    "budget_breakdown": {
        "accommodation": 1000,
        "transportation": 600,
        "food_and_dining": 400,
        "activities_and_tours": 300,
        "miscellaneous": 200,
    },
}