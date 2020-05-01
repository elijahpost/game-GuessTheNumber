# readme
# game-GuessTheNumber
My first reasonably put together python program. Runs in python command line.
Requires Python3.

The program is a more complicated version of the "Writing a Guess-The-Number Program"
section in the Udemy Version of @asweigart's "Automate the Boring Stuff with Python"
book for beginner programmers using python.

Why do this?
1. Test the assumption that jamming renders creativity in code just as it does in music.
	I'm as much a sucker for feature-creep as others. Generally, I see feature-creep as
	a bad thing, but I am allowing it to some extent as long as it contributes to reenforcing
	new concepts that I am learning. In essence, I'm allowing myself creative space to add new
	features to the program since the scope of the project is to learn, just as the scope of a
	musical jam sesh is generally to produce inspired creative output.
2. (re)Learn git.
	Throwing this on github, and taking a few tutorials, will allow me to get back up to speed
	using git, which I learned and largely unlearned a few years back. I see familiarity with
	git as an absolutly essential component to my software education and my hirability.
3. Build a portfolio.
	Equally essential to my education and hirability is documented history of code contribution.
	My history begins with this project.

I expect to modify this project as I learn new skills.

What makes it more complicated?
1. Added features, discussed below.
2. The vast majority of the code is defined functions, as I understand a program should be written.

Features over and above those defined in the example program:
1. Version Checker:
	The program cannot run without Python3 and will display a message to that end if executed in an older
	version of python.
2. Multiple levels:
	How: The level() function accepts four arguments which define the level. main() calls the function as
	many times as there are levels in the game. Level parameters are currently hardcoded into main().
3. Scorekeeping:
	Upon completion of the level, the user's level score (the number of guesses they still had remaining)
	is tallied and added to the user's game score. Both scores are displayed at the end of each level and
	at the conclusion of the game.
4. Messaging:
	A number of functions including welcome(), gameOver(), levelClear(), gameClear, and restartPrompt() are
	there to guide the player through the game, displaying information and asking for inputs to determine the
	next thing to do. restartPrompt() uses sys.exit to return the user back to shell if instructed by user input.
	
Known Issues:
	Entering a non-integer on your last available guess will cause the program to crash.

Ideas for more features down the row:
 - It would be kinda tight to save a user's high score for retriveal later.
 - GUI overlay
 - Compile the project into an executable
 - Create an installer
 - Additional game modes
