# Gobang

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/kerong2002/Gobang_Socket/assets/70834651/9d4a386b-0e8a-4e28-a0dd-4e313a7f6ace" height="450">
      <br>
      Server
    </td>
    <td align="center">
      <img src="https://github.com/kerong2002/Gobang_Socket/assets/70834651/8501d646-8b91-426b-8c85-aebc81ae6f48" height="450">
      <br>
      Client
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="center">
      <img src="/TCP.png" height="450">
    </td>
    <td align="center">
      <img src="/UDP.png" height="450">
    </td>
  </tr>
</table>


- Starting the game requires two parameters, the **IP address** of the host and the **port number**. 
- For example, you can start the game with the following command:
```py
python Gobang_server.py <ip_address> <port_number>
python Gobang_client.py <ip_address> <port_number>
# example:
python Gobang_server.py localhost 1234
python Gobang_client.py localhost 1234
```

- In the game, black moves first. You can place a piece by clicking on a position on the board with your mouse. When it is your turn to move, a prompt will appear on the screen indicating that it is your turn.

- During the game, you can right-click on the board to view the game rules and to surrender. When a player wins or surrenders, the game will end and both players will be prompted to play again.

- That's it! Enjoy playing Gobang via UDP socket.
