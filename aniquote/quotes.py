def quote():

    # Define a dictionary containing the names of anime characters and their famous dialogues
    characters = {
        "Naruto": "Believe it!",
        "Itachi": "People’s lives don’t end when they die, it ends when they lose faith.",
        "Uchiha Itachi": "You are already under my Genjutsu !",
        "Goku": "Kamehameha!",
        "Luffy": "I'm gonna be king of the pirates!",
        "Saitama": "Ok.",
        "Ichigo": "Bankai!",
        "Gildarts": "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.",
        "Vegeta": "It's over 9000!",
        "Kaneki": "I am not the protagonist of my own life.",
        "Light": "I am justice!",
        "Spike": "Bang!",
        "Edward": "Equivalent exchange!",
        "Naruto Uzumaki": "I won't run away anymore... I won't go back on my word... that is my ninja way!",
        "Sasuke Uchiha": "It's not like I ever went around believing in myself. I just believed in the power of my comrades.",
        "Sakura Haruno": "Shannaro!",
        "Kakashi Hatake": "I'm Kakashi Hatake. Things I like and things I hate...I don't feel like telling you that. My dreams for the future...never really thought about it. As for my hobbies...I have lots of hobbies.",
        "Itachi Uchiha": "People live their lives bound by what they accept as correct and true. That's how they define 'reality'. But what does it mean to be 'correct' or 'true'? Merely vague concepts... their reality may all be a mirage. Can we consider them to simply be living in their own world, shaped by their beliefs?",
        "Jiraiya": "A person grows up when he's able to overcome hardships. Protection is important, but there are some things that a person must learn on his own.",
        "Tsunade": "I'm going to become a great ninja. A ninja who can stand above all, a ninja who can surpass all the Hokage before me!",
        "Minato Namikaze": "I'm a shinobi of Konoha. I'm not going to run away!",
        "Hinata Hyuga": "I used to always cry and give up... I made many wrongs turns... But you... You helped me find the right path... I always chased after you... I wanted to catch up to you... I wanted to walk beside you all the time... I just wanted to be with you... You changed me! Your smile is what saved me! That is why I'm not afraid to die protecting you! Because... I love you...",
        "Neji Hyuga": "When one person is cursed, two graves are dug.",
        "Rock Lee": "A dropout will beat a genius through hard work.",
        "Gaara": "I love only myself and fight only for myself. And as long as I think everybody exists to make me feel that way... the world is wonderful.",
        "Kiba Inuzuka": "It's not the face that makes someone a monster, it's the choices they make with their lives.",
        "Shino Aburame": "The weak are meat, and the strong do eat.",
        "Temari": "The most important thing for a shinobi is to know oneself.",
        "Kankuro": "People, who continue to put their lives on the line to defend their faith become heroes and those who lose faith... become mere men.",
        "Shikamaru Nara": "What a drag.",
        "Ino Yamanaka": "I don't care about who I was. I'm just living in the present and taking the good things from the past.",
        "Chouji Akimichi": "I always thought that you became a hero when you saved someone else. But... you can also become one by saving yourself.",
        "Asuma Sarutobi": "All people feel fear. Whether they're beginners or veterans. A person who conquers fear is a true warrior.",
        "Kurenai Yuhi": "You can't become Hokage if you don't have friends.",
        "Jugo": "I'll lend you my power until you find your own.",
        "Karin": "The thing about love is that it's useless in battle.",
        "Suigetsu Hozuki": "I'm not a tool. Don't treat me like I'm nothing.",
        "Orochimaru": "It is not wise to judge others based on your own preconceptions and by their appearances.",
        "Tobi": "The true measure of a shinobi is not how he lives, but how he dies.",
        "Madara Uchiha": "Power is not will, it is the phenomenon of physically making things happen.",
        "Hashirama Senju": "There is no such thing as true peace. It is simply a matter of who has the power to enforce their will upon others.",
        "Tobirama Senju": "In battle, it's important to have a sense of humor.",
        "Hiruzen Sarutobi": "The true measure of a shinobi is not how he lives, but how he dies.",
        "Obito Uchiha": "Those who break the rules are scum, but those who abandon their friends are worse than scum.",
        "Kaguya Otsutsuki": "The moment people come to know love, they run the risk of carrying hate.",
        "Killer Bee": "You can't touch music, but music can touch you.",
        "Nagato": "People become stronger because they have things they cannot forget. That's what you call growth.",
        "Konan": "You don't become a Hokage to be acknowledged by everyone. The one who is acknowledged by everyone becomes the Hokage.",
        "Sai": "If you don't like your destiny, don't accept it. Instead, have the courage to change it the way you want it to be.",
        "Yamato": "The purpose of training is to tighten up the slack, toughen the body, and polish the spirit.",
        "Shizune": "The body ages, but the heart remains young.",
        "Iruka Umino": "In the ninja world, those who break the rules are scum, that's true, but those who abandon their friends are worse than scum.",
        "Anko Mitarashi": "The difference between stupidity and genius, is that genius has its limits.",
        "Kabuto Yakushi": "Power is not something that can be obtained easily. It requires sacrifice.",
        "Deidara": "Art is an explosion!",
        "Sasori": "The only way to escape the abyss is to look at it, gauge it, sound it out and descend into it.",
        "Hidan": "There's no greater joy than killing your enemies!",
        "Kakuzu": "Money is the key to everything in this world.",
        "Zabuza Momochi": "In the shinobi world, those who break the rules are scum, that's true, but those who abandon their friends are worse than scum.",
        "Haku": "Those who forgive themselves, and are able to accept their true nature... They are the strong ones!",
        "Kimimaro": "The only thing that truly satisfies me is death.",
        "Gaara's father": "The true power is the power to take life, and it is the principle that governs the world of shinobi.",
        "Tenten": "I want to show them that infinite possibilities await those who are brave enough to seek them.",
        "Lee": "Gai-sensei is always saying that youth is power. But what is youth? I don't think it's something that can be measured in time.",
        "Monkey D. Luffy": "I don't want to conquer anything. I just think that the guy with the most freedom in this whole ocean is the Pirate King!",
        "Roronoa Zoro": "I don't know how to give up and die!",
        "Nami": "There's no such thing as a hero who doesn't make mistakes.",
        "Usopp": "Men who can't wipe away the tears from women's eyes aren't real men.",
        "Sanji": "You don't understand... I don't want to kick women. I just want to kick you.",
        "Tony Tony Chopper": "If I can't protect my captain's dream, then whatever ambition I have is nothing but talk.",
        "Nico Robin": "I want to live! Take me out to sea with you!",
        "Franky": "The weak don't get to decide anything, not even how they die.",
        "Brook": "What good is treasure if I'm alone? After sharing so much of our dreams instead of sacrificing them and leaving with you. I would rather have nothing at all!",
        "Jinbe": "The strength of a pirate is not measured by how many ships he has, but by the loyalty of his crew.",
        "Portgas D. Ace": "No matter how hard or impossible it is, never lose sight of your goal.",
        "Boa Hancock": "My beauty is everything!",
        "Dracule Mihawk": "What is a swordsman without his sword?",
        "Donquixote Doflamingo": "Pirates are evil? The Marines are righteous? These terms have always changed throughout the course of history! Kids who have never known peace have different values than those who have never known war. Those who stand at the top determine what's wrong and what's right! Justice will prevail, you say? But of course it will! Whoever wins this war becomes justice!",
        "Bartholomew Kuma": "You can't bring back what you've lost, think about what you have now!",
        "Blackbeard": "The only thing we're allowed to do is believe. We can't change anything.",
        "Buggy the Clown": "My dream is to become a pirate who's respected by everyone!",
        "Eustass Kid": "People who put themselves above others are the lowest of the low.",
        "Trafalgar Law": "The weak don't get to decide anything, not even how they die.",
        "X Drake": "What's important is not how many lives you have, but how you live them.",
        "Capone Bege": "The world is a sea of treasures, and there's just as much trash mixed in with it.",
        "Carrot": "Dreams are worth fighting for!",
        "Gol D. Roger": "My treasure? If you want it, I'll let you have it. Look for it! I left everything in that place!",
        "Silvers Rayleigh": "You see, to be able to achieve something that hasn't been done before, that's what makes life worth living.",
        "Kaido": "If you don't want to die, don't make an enemy out of me.",
        "Charlotte Linlin": "The weak have no rights or choices! That is the natural order of the world!",
        "Marshall D. Teach": "There are some things in this world you can never change, no matter how hard you try.",
        "Smoker": "If I have to fight for something, I'll fight for my own sake",
        "Ichigo Kurosaki": "I'll take responsibility for what I've done. If I must fall, I'll rise each time a better man.",
        "Rukia Kuchiki": "I'm not a warrior. I'm a soldier who was thrown away.",
        "Renji Abarai": "I am not some pawn to be sacrificed!",
        "Byakuya Kuchiki": "It is not because I care about you. It is because I care about my pride.",
        "Kenpachi Zaraki": "The only reason why people do not know much is because they do not care to know. They are incurious. Incuriousity is the oddest and most foolish failing there is.",
        "Toshiro Hitsugaya": "Standing there trembling, you look like a flower about to fall. But know... even if you fall, your bloom will live on. I will not let you wilt.",
        "Gin Ichimaru": "The difference between a king and his horse is that the king can make decisions.",
        "Ulquiorra Cifer": "To know sorrow is not terrifying. What is terrifying is to know you can't go back to happiness you could have.",
        "Sosuke Aizen": "If one were to turn into a vegetable, one would be better off dead, since the sensation of life would not exist.",
        "Orihime Inoue": "I've decided to believe in myself. Not in the me who believes in you. Not in the you who believes in me. But in the me who believes in myself.",
        "Uryu Ishida": "I am the son of the leader of the Quincy. Whether I'm traitor or not, I will not allow anyone to threaten the world that my father loved so much.",
        "Yoruichi Shihoin": "I told you, didn't I? I don't want to rule the world. I just want to be strong enough to protect what matters most to me.",
        "Kisuke Urahara": "The difference between stupidity and genius is that genius has its limits.",
        "Mayuri Kurotsuchi": "If you were to turn into a snake tomorrow, and begin devouring humans, and from the same mouth, you started devouring animals, birds, insects, and so on, and continue to do so day after day, then, I believe, you would eventually turn into a dragon.",
        "Yamamoto Genryusai": "You may have thought you could defeat me if you learned Bankai, but there is a reason that it is the last secret of the Shinigami.",
        "Grimmjow Jaegerjaquez": "You got it all wrong. It's not about dying for your ideals. It's about killing for them.",
        "Sajin Komamura": "I will not let anyone else be sacrificed. Not when I can protect them.",
        "Nelliel Tu Odelschwanck": "It doesn't matter if I'm a monster to you... but if I'm a monster to my friends, then that's a different story!",
        "Tier Harribel": "I do not fear death. I fear only that my rage will fade over time.",
        "Szayelaporro Grantz": "I am the ruler of this world, the king of Hueco Mundo, the god of all creation.",
        "Kaname Tosen": "There is no such thing as a good or evil person. I believe that all humans are equal, regardless of their race, religion or gender.",
        "Frieza": "The true measure of a warrior is not his strength, but his willingness to fight for what he believes in.",
        "Beerus": "I am the God of Destruction. Even the concept of good and evil are meaningless to me.",
        "Whis": "The only way to become a God is to think like one.",
        "Jiren": "Strength is justice. Strength is absolute. Everything else is meaningless.",
        "Hit": "Time doesn't matter to me. If it's necessary, I can even stop time. But for me, it's the present that's important.",
        "Kale": "I'm not a monster! I'm just someone who's always been alone!",
        "Caulifla": "I'll get as strong as I need to be. I'm not going to limit myself!",
        "Cabba": "Being strong is not just about physical strength. It's also about the strength of your heart.",
        "Toppo": "I am a warrior of justice. It is my duty to protect the peace and order of the universe.",
        "Android 17": "I don't care about becoming stronger. All I care about is protecting this planet and the animals that live on it.",
        "Android 18": "I don't care about power. I just want to live my life with my family.",
        "Gohan": "Power comes in response to a need, not a desire. You have to create that need.",
        "Piccolo": "The power comes in response to a need, not a desire. You have to create that need.",
        "Krillin": "I may not have the power of a Saiyan, but I have the heart of a warrior!",
        "Master Roshi": "Training is not just about physical exertion. It's also about training the mind and the spirit.",
        "Champa": "I am the God of Destruction of Universe 6. Don't mess with me!",
        "Vados": "The role of an angel is to guide the God of Destruction, not to interfere in mortal affairs.",
        "Zeno": "I am the king of everything. I can erase anything I want.",
        "Grand Priest": "I am the Grand Priest. My duty is to serve the Omni-King and to maintain balance in the multiverse.",
        "Majin Buu": "I'm sorry, I got carried away and turned you into chocolate. Would you like me to change you back?",
        "Hit": "I don't kill my opponents, I erase them from existence.",
        "Gowasu": "As a God, it is my duty to watch over the universe and ensure that peace is maintained.",
        "Zamasu": "The world is full of contradictions. It's time to eliminate them all.",
        "Frost": "I may not be the strongest, but I'm certainly the smartest.",
        "Hit": "Time is a valuable resource. Use it wisely.",
    }

    # Get the name of the anime character from the user
    name = input(
        "Enter the name of an anime character with first letter capital :  ")

    # Check if the character is in the dictionary
    if name in characters:
        # If the character is in the dictionary, print their famous dialogue
        print(characters[name])
    else:
        # If the character is not in the dictionary, print an error message
        print("Sorry, I don't know that character.")


