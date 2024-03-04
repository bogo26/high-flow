// import "./App.css";

import React from "react";
import useWebSocket from "react-use-websocket";

const App = () => {
  const { sendJsonMessage } = useWebSocket("ws://127.0.0.1:8000/ws/chat/", {
    onOpen: () => console.log("opened"),
    //Will attempt to reconnect on all close events, such as server shutting down
    shouldReconnect: (closeEvent) => true,
});

  // Function to send a message
  const sendMessage = () => {
      const message = { type: "chat", message: "Hello, WebSocket!" };
      console.log("Sending message:", message);
    sendJsonMessage(message);
  };

  return (
    <div>
      <button onClick={sendMessage}>Send Message</button>
    </div>
  );
};

export default App;
