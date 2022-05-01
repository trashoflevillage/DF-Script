
definedTokens = {
    "{" : "openBrace",
    "}" : "closeBrace",
    "@" : "subscribeToken",
    "(" : "openParen",
    ")" : "closeParen",
    ";" : "end"
}

def tokenize(contents:str):
    tokens = []
    location = 0
    while location < len(contents):
        char:str = contents[location]
        if char.isalpha() or char == "_":
            buffer = ""
            while contents[location].isalnum():
                location += 1
                buffer = buffer + contents[location]
        location += 1
            
    
# identifier: playerJoin
# subscribeToken
# identifier: PlayerJoinEvent
# openBrace
# comment
# end
# identifier: select
# identifier: ALL
# end
# identifier: Player
# dotOperator
# identifer: sendMessage
# openParen
# string: "%default has joined the game!"
# close Paren
# closeBrace