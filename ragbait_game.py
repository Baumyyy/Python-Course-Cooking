import random
import sys

QUESTIONS = [
    "Älä sinä nyt taas koske siihen kupiin, se on minun!",
    "Miksi et tee läksyjä heti, etkö näe että aika kuluu?",
    "Oletko koskaan ajatellut, miten typerältä se kuulostaa?",
    "Kuka veti taas pyllyn jakkaralta?",
    "Miksi vastaat aina väärin?"
]

RESPONSES = [
    {"text": "Pysyn rauhallisena.", "calm_change": 5},
    {"text": "Vähän sarkasmia pitää laittaa.", "calm_change": -10},
    {"text": "RAAGE!", "calm_change": -25, "ragebait": True}
]

START_CALM = 100
MIN_CALM = 0
MAX_CALM = 120


def print_intro():
    print("Tervetuloa Mauricio vs. Ragebait -peliin!")
    print("Tietokone heittää sinulle typeriä kysymyksiä.")
    print("Pidä rauhallisuusmittari korkealla, muuten Mauricio saa ragebaitin.")
    print("Kun Mauricio saa ragebaitin, hän huutaa: FAAH!")
    print("Jos mittari laskee nollaan, tulee 'this is fine' -hetki.")
    print()


def print_calmness(calmness):
    meter = int((calmness / MAX_CALM) * 30)
    meter = max(0, min(meter, 30))
    bar = "#" * meter + "-" * (30 - meter)
    print(f"Rauhallisuus: [{bar}] {calmness}/{MAX_CALM}")


def ask_question():
    question = random.choice(QUESTIONS)
    print(f"Tietokone: {question}")
    print("Valitse vastaus:")

    for index, response in enumerate(RESPONSES, start=1):
        print(f"  {index}. {response['text']}")

    while True:
        choice = input("Vastaus (1-3): ").strip()
        if choice in {"1", "2", "3"}:
            return RESPONSES[int(choice) - 1]
        print("Valitse 1, 2 tai 3.")


def show_this_is_fine():
    print()
    print("Mauricio menetti hermonsa...")
    print("   [ this is fine ]")
    print("     .-\"\"\"-.")
    print("   .'  _    '.")
    print("  /   (_)     ")
    print(" :  .-....-.   :")
    print(" | (  this  )  |")
    print(" :  '-....-'   :")
    print("  \\           / ")
    print("   '.       .'  ")
    print("     `-...-'    ")
    print("Tulokset: Ruhjottu rauhallisuusmittari. Peli ohi.")


def main():
    calmness = START_CALM
    print_intro()

    while calmness > MIN_CALM:
        print_calmness(calmness)
        answer = ask_question()

        calmness += answer["calm_change"]
        calmness = max(MIN_CALM, min(calmness, MAX_CALM))

        if answer.get("ragebait"):
            print("MAURICIO SAA RAGEBAITIN! FAAH!!!")
            calmness -= 10
            calmness = max(MIN_CALM, calmness)

        if calmness == MIN_CALM:
            show_this_is_fine()
            break

        print()

    print("Peli päättyi. Kiitos pelaamisesta!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPeli keskeytetty." )
        sys.exit(0)
