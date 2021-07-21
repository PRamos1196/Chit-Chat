import React, { useState, useRef } from 'react';
import Chat from './Chat'; // Grabs "chat" from current directory
import { Socket } from './Socket';
import { GoogleButton } from './GoogleButton';

export default function Main() {
  // Default state is an empty chat (no messages sent)
  // messages = every message is conversation state
  // setMessages = function to update conversation
  const [setMessages] = useState([]);
  const [count, setCount] = useState(0);
  const messageContentsRef = useRef();
  const [onetime, setOneTime] = useState(true);
  const [send, setSent] = useState([]);
  const [accounts, setAccounts] = useState([]);

  const [user, setUsers] = useState([]);
  const [setEmails] = useState([]);
  const [url, setUrl] = useState([]);
  const [login, setLogin] = useState(false);

  function populates(dbMessage, dbUser, dbUrl, urlCheck) {
    const listMessage = [];
    for (let i = 0; i < dbMessage.length; i += 1) {
      console.log(dbMessage[i].message);
      console.log(urlCheck[i].type);
      if (urlCheck[i].type === 'msg') {
        listMessage.push(<div key={i}>
          <img className="profile-pic" src={dbUrl[i].urls} />
          <p className="userName">{dbUser[i].username}</p>
          <p className="textmessage">{dbMessage[i].message}</p>
        </div>);
      } else if (urlCheck[i].type === 'img') {
        listMessage.push(<div key={i}>
          <img className="profile-pic" src={dbUrl[i].urls} />
          <p className="userName">{dbUser[i].username}</p>
          <img className="textmessage" src={dbMessage[i].message} />
        </div>);
      } else {
        listMessage.push(<div key={i}>
          <img className="profile-pic" src={dbUrl[i].urls} />
          <p className="userName">{dbUser[i].username}</p>
          <a className="textmessage" href={dbMessage[i].message}>{dbMessage[i].message}</a>
                         </div>);
      }
    }
    setSent(listMessage);
  }

  React.useEffect(() => { Socket.on('message_history', (data) => { populates(data.allMessages, data.allUsers, data.allUrls, data.typeOf); }); });
  React.useEffect(() => { Socket.on('count', (data) => { setUsers(data.username); setCount(data.count); }); });

  function getAllAccounts() {
    React.useEffect(() => {
      Socket.on('accounts received', (data) => {
        const allAccounts = data.allUsers;
        console.log(`Received accounts from server: ${allAccounts}`);
        setAccounts(allAccounts, []);
      });
    });
  }

  function setLoginTest(bool) {
    setLogin(bool);
  }

  function setUsersTest(event) {
    setUsers(event);
  }

  function setEmailsTest(event) {
    setEmails(event);
  }

  function setUrlsTest(event) {
    setUrl(event);
  }

  function onetimecall() {
    if (onetime) {
      Socket.emit('onetime');
      setOneTime(false);
    }
  }
  // console.log(messages);

  function messageHandler() {
    const contents = messageContentsRef.current.value;

    if (contents === '') return;
    setMessages((prevMessages) => [
      { contents },
      ...prevMessages,
    ]);

    messageContentsRef.current.value = null; // clears the input value
    console.log(user);

    Socket.emit('new-messages', {
      username: user,
      message: contents,
      url,
    });
  }

  console.log(accounts);
  getAllAccounts();
  onetimecall();

  return (
    // Wrap multiple items in empty tag so we only return "one" thing
    <div>
      {login === false
        ? (
          <div className="Login-Box">
            <GoogleButton
              setLogin={setLoginTest}
              setUsers={setUsersTest}
              setEmail={setEmailsTest}
              setUrl={setUrlsTest}
            />
          </div>
        )
        : (
          <div id="box" className="box">
            <div className="chitChat">
              <div className="users-online"><p className="userCount">{count}</p></div>
              <div className="text-space">
                <Chat messages={send} />
              </div>
              <div className="message-send">
                <button className="message-btn" onClick={messageHandler}>
                  Send
                </button>
                <input
                  className="text-bar"
                  ref={messageContentsRef}
                  type="text"
                  placeholder="Message here"
                />
              </div>
            </div>
          </div>
        )}
    </div>
  );
}
