# app.py
import streamlit as st

from chat_companion import get_ai_response
from sample_data import SAMPLE_TRIP_DATA


st.set_page_config(
    page_title="Safar AI Travel Companion",
    page_icon="🌍",
    layout="wide",
)


def initialize_session_state():
    """Create chat history when the app starts."""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_trip_sidebar(trip_data):
    """Display trip information in the sidebar."""

    st.sidebar.header("🧳 Your Trip")

    st.sidebar.write(
        f"**Traveler:** {trip_data.get('traveler_name', 'Guest')}"
    )

    st.sidebar.write(
        f"**Country:** {trip_data.get('country', 'Not provided')}"
    )

    st.sidebar.write(
        f"**Travelers:** "
        f"{trip_data.get('number_of_travelers', 'Not provided')}"
    )

    budget = trip_data.get("budget", "Not provided")
    currency = trip_data.get("currency", "")

    st.sidebar.write(f"**Budget:** {budget} {currency}")

    st.sidebar.write(
        f"**Duration:** "
        f"{trip_data.get('duration_days', 'Not provided')} days"
    )

    st.sidebar.write("**Cities:**")

    for city in trip_data.get("cities", []):
        st.sidebar.write(f"- {city}")

    st.sidebar.divider()

    if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.sidebar.divider()

    st.sidebar.caption(
        "Safar provides general travel guidance. "
        "Always verify current information with official or trusted sources."
    )


def display_itinerary(trip_data):
    """Display the current itinerary."""

    with st.expander("📅 View Current Itinerary"):
        itinerary = trip_data.get("itinerary", [])

        if not itinerary:
            st.info("No itinerary is currently available.")
            return

        for day in itinerary:
            day_number = day.get("day", "?")
            city = day.get("city", "Unknown city")

            st.markdown(f"### Day {day_number} — {city}")

            for activity in day.get("activities", []):
                st.write(f"- {activity}")


def display_budget(trip_data):
    """Display the estimated budget breakdown."""

    with st.expander("💰 View Budget Breakdown"):
        breakdown = trip_data.get("budget_breakdown", {})

        if not breakdown:
            st.info("No budget information is currently available.")
            return

        for category, amount in breakdown.items():
            formatted_category = category.replace("_", " ").title()
            currency = trip_data.get("currency", "")

            st.write(
                f"**{formatted_category}:** {amount} {currency}"
            )


def main():
    initialize_session_state()

    # Temporary sample data.
    # Later, replace this with data from your team's main application.
    trip_data = SAMPLE_TRIP_DATA

    st.title("🌍 Safar AI Travel Companion")

    st.subheader(
        "Your helpful local companion while exploring Pakistan"
    )

    st.write(
        "Ask about Pakistani culture, food, transport, Urdu translations, "
        "packing, safety, or changes to your itinerary."
    )

    display_trip_sidebar(trip_data)
    display_itinerary(trip_data)
    display_budget(trip_data)

    st.divider()

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    user_message = st.chat_input(
        "Ask Safar a question..."
    )

    if user_message:
        # Save and display the user's message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        with st.chat_message("user"):
            st.markdown(user_message)

        # Generate the AI response
        with st.chat_message("assistant"):
            with st.spinner("Safar is thinking..."):
                response = get_ai_response(
                    user_message=user_message,
                    chat_history=st.session_state.messages[:-1],
                    trip_data=trip_data,
                )

            st.markdown(response)

        # Save the assistant's response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )


if __name__ == "__main__":
    main()
