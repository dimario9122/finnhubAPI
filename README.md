Getting information from Finnhub API

Actors: User, System.
User Objective: Get information about the ETF.
The purpose of the system is to display information about the ETF in a readable form to the user.
Main scenario:
1) The user starts the system. The system opens a user session and offers to select an ETF.
2) The user selects the ETF using a sequence number.
3) The system checks the correctness of the selected number.
4) The system offers to select several types of information that the user may need.
5) The system displays the information to the user that was obtained during the system's call to the Finnhub API.
Result: The system received and processed information from the Finnhub API. The user has received the processed information.
Extensions:
1) The user entered an incorrect ETF number.
The system again provides ETF selection.
Result: The user does not reach the next stage.
2) The user entered an invalid function number to retrieve information about the ETF.
The system again provides a selection of functions for obtaining ETF information.
Result: The user does not receive information about the ETF.