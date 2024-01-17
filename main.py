import eulerChallenges
import inputOutput
print(type(eulerChallenges.eulerchallenge1()))
# Ask the user what challenge to calculate
eulerChallengeNr = inputOutput.askinput()

# Run function accosiated with user input number to calculate specific Euler Challenge
challengeAnswer = inputOutput.runfunction(eulerChallengeNr)

# Print challenge results
inputOutput.checkresult(challengeAnswer)


