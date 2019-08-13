def createDeck(options):
        if options["deckSize"] < 1:
                print('Deck size must be a positive number')
        else: 
                createdDeck = []
                for deck in range(options["deckSize"]):
                        for suit in range(options["numberOfSuites"]):
                                for value in range(options["suiteLimit"]):
                                        card = {
                                                "Suit": suit,
                                                "Value": value
                                        }
                                        # print(card)
                                        createdDeck.append(dict(card))
                        
                        
                
                return createdDeck
        
deckOptions = {
        "deckSize": 1,
        "numberOfSuites": 4,
        "suiteLimit": 13
}
deck = createDeck(deckOptions)
print(deck)
print(len(deck))
