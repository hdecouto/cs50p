SHOWS = [
    " avatar: The Last Airbender",
    "Ben 10",
    "Arthur",
    " spongeBob SquarePants",
    "Phineas and Ferb",
    "Kim Possible",
    "Jimmy Neutron",
    "The Proud Family"
    ]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
  
    print(','.join(cleaned_shows))

if __name__ == "__main__":
    main()