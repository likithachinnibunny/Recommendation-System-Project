from recommender import recommend_movies

def main():
    user_choice = input("Enter preferred genre (Action/Comedy/Horror/Drama): ")
    recommendations = recommend_movies(user_choice)

    if recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations:
            print("-", movie)
    else:
        print("No recommendations found.")

if __name__ == "__main__":
    main()
