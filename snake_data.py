from database import connect

def insert_snakes():
    conn = connect()
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM snakes")

    snakes = [
        ("King Cobra", "Ophiophagus hannah", "Yes", 4.0, "Forest", "India, Southeast Asia", "Snakes", "Vulnerable"),
        ("Indian Python", "Python molurus", "No", 3.5, "Forest, Grassland", "India", "Mammals, Birds", "Near Threatened"),
        ("Black Mamba", "Dendroaspis polylepis", "Yes", 3.0, "Savanna", "Sub-Saharan Africa", "Mammals, Birds", "Least Concern"),
        ("Green Anaconda", "Eunectes murinus", "No", 5.0, "Swamp, River", "South America", "Mammals, Fish", "Least Concern"),
        ("Reticulated Python", "Malayopython reticulatus", "No", 4.5, "Forest", "Southeast Asia", "Mammals, Birds", "Least Concern"),
        ("Gaboon Viper", "Bitis gabonica", "Yes", 1.5, "Rainforest", "Africa", "Mammals", "Least Concern"),
        ("Russell's Viper", "Daboia russelii", "Yes", 1.2, "Grassland", "South Asia", "Rodents", "Least Concern"),
        ("Boomslang", "Dispholidus typus", "Yes", 1.5, "Forest", "Sub-Saharan Africa", "Birds, Reptiles", "Least Concern"),
        ("Eastern Coral Snake", "Micrurus fulvius", "Yes", 0.8, "Forest", "USA", "Small reptiles", "Least Concern"),
        ("Timber Rattlesnake", "Crotalus horridus", "Yes", 1.2, "Forest", "Eastern USA", "Rodents", "Least Concern"),
        ("Copperhead", "Agkistrodon contortrix", "Yes", 0.9, "Woodland", "USA", "Rodents", "Least Concern"),
        ("Ball Python", "Python regius", "No", 1.5, "Grassland", "West Africa", "Rodents", "Near Threatened"),
        ("Burmese Python", "Python bivittatus", "No", 4.0, "Forest, Wetland", "Southeast Asia", "Mammals", "Vulnerable"),
        ("Inland Taipan", "Oxyuranus microlepidotus", "Yes", 1.8, "Desert", "Australia", "Rodents", "Least Concern"),
        ("Coastal Taipan", "Oxyuranus scutellatus", "Yes", 2.0, "Coastal Forest", "Australia", "Mammals", "Least Concern"),
        ("Corn Snake", "Pantherophis guttatus", "No", 1.2, "Grassland", "USA", "Rodents", "Least Concern"),
        ("Milk Snake", "Lampropeltis triangulum", "No", 1.0, "Forest", "North America", "Rodents", "Least Concern"),
        ("King Snake", "Lampropeltis getula", "No", 1.2, "Forest", "North America", "Rodents, Reptiles", "Least Concern"),
        ("Indian Cobra", "Naja naja", "Yes", 1.5, "Forest, Farmland", "India", "Rodents", "Least Concern"),
        ("Egyptian Cobra", "Naja haje", "Yes", 1.8, "Desert", "North Africa", "Rodents", "Least Concern"),
        ("Western Diamondback Rattlesnake", "Crotalus atrox", "Yes", 1.5, "Desert", "USA, Mexico", "Rodents", "Least Concern"),
        ("Puff Adder", "Bitis arietans", "Yes", 1.0, "Savanna", "Africa", "Mammals", "Least Concern"),
        ("Bushmaster", "Lachesis muta", "Yes", 2.5, "Rainforest", "Central America", "Mammals", "Least Concern"),
        ("Carpet Python", "Morelia spilota", "No", 2.0, "Forest", "Australia", "Mammals, Birds", "Least Concern"),
        ("Rat Snake", "Ptyas mucosa", "No", 2.0, "Grassland", "South Asia", "Rodents", "Least Concern")
    ]

    cursor.executemany("""
    INSERT INTO snakes
    (name, scientific_name, venomous, average_length, habitat, region, diet, conservation_status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, snakes)

    conn.commit()
    conn.close()

    print("25 snakes inserted successfully!")

insert_snakes()