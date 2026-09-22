
import random


movies_list = [
    "Aavesham",
    "Premalu",
    "Manjummel Boys",
    "Bramayugam",
    "Romancham",
    "Kannur Squad",
    "RDX",
    "2018",
    "Jaya Jaya Jaya Jaya Hey",
    "Hridayam",
    "Kumbalangi Nights",
    "Joji",
    "Drishyam",
    "Drishyam 2",
    "Bangalore Days",
    "Premam",
    "Charlie",
    "Lucifer",
    "Neru",
    "Thudarum",
    "Dangal",
    "3 Idiots",
    "Zindagi Na Milegi Dobara",
    "Dil Chahta Hai",
    "Lagaan",
    "Sholay",
    "Jab We Met",
    "Bajrangi Bhaijaan",
    "Chhichhore",
    "PK",
    "Andhadhun",
    "Drishyam",
    "Queen",
    "Barfi",
    "Taare Zameen Par",
    "Munna Bhai M.B.B.S.",
    "Kahaani",
    "Gully Boy",
    "Jawan",
    "Pathaan",
    "Kaithi",
    "Vikram",
    "Master",
    "Leo",
    "Jailer",
    "Maharaja",
    "96",
    "Vada Chennai",
    "Asuran",
    "Soorarai Pottru",
    "Jai Bhim",
    "Ratsasan",
    "Vikram Vedha",
    "Thani Oruvan",
    "Ghilli",
    "Enthiran",
    "2.0",
    "Ponniyin Selvan",
    "Sivaji",
    "Anniyan",
    "Baahubali",
    "Baahubali 2",
    "RRR",
    "Pushpa",
    "Pushpa 2",
    "Arjun Reddy",
    "Jersey",
    "Eega",
    "Ala Vaikunthapurramuloo",
    "Rangasthalam",
    "Salaar",
    "Kalki 2898 AD",
    "Devara",
    "Sita Ramam",
    "Hi Nanna",
    "Major",
    "Dasara",
    "Agent",
    "Temper",
    "Janatha Garage",
    "KGF",
    "KGF Chapter 2",
    "Kantara",
    "777 Charlie",
    "Lucia",
    "Kirik Party",
    "U Turn",
    "Dia",
    "Garuda Gamana Vrishabha Vahana",
    "Charlie 777"
]

chance = 6
movie_selected = random.choice(movies_list)


letter_count = len(movie_selected)
guessed_chars = guessed_movie = ""

for i in range(len(movie_selected)):
    if movie_selected[i] == " ":
        print("",end="")
    else:
        print('-', end="")
print()

while chance > 0:
    usr_char = input("Enter a character: ")
    if usr_char.lower() in movie_selected.lower():
        guessed_chars = guessed_chars + usr_char.lower()
        guessed_movie = ""
        for i in range(len(movie_selected)):
            if movie_selected[i].lower() in guessed_chars:
                print(movie_selected[i], end="")
                guessed_movie = guessed_movie + movie_selected[i]
            elif movie_selected[i] == " ":
                print(" ", end="")
                guessed_movie = guessed_movie + " "
            else:
                print("-", end="")
                guessed_movie = guessed_movie +"-"
        print()
    else:
        chance = chance - 1
        print("Wrong character!")
        print(f"You have {chance} left")
        guessed_movie = ""
        for i in range(len(movie_selected)):
                    if movie_selected[i].lower() in guessed_chars:
                        print(movie_selected[i], end="")
                        guessed_movie = guessed_movie + movie_selected[i]
                    elif movie_selected[i] == " ":
                        print(" ", end="")
                        guessed_movie = guessed_movie + " "
                    else:
                        print("-", end="")
                        guessed_movie = guessed_movie +"-"
        print()
    if "-" not in guessed_movie:
         print("Congratulations! You guessed the movie !")
         break
    if chance == 0:
         print("Zero chances.Game over!")
         print(f"Movie was {movie_selected}")
        

        

