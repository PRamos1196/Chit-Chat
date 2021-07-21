import React, { useState } from 'react';
import GoogleLogin from 'react-google-login';
import { Socket } from './Socket';

export function GoogleButton(props) {
  const [user, setUser] = useState('');
  const [email, setEmail] = useState('');
  const [url, setUrl] = useState('');

  function handleSubmit(response) {
    console.log(response);
    setUser(response.profileObj.name);
    setEmail(response.profileObj.email);
    setUrl(response.profileObj.imageUrl);

    Socket.emit('new google user', {
      name: response.profileObj.name,
      email: response.profileObj.email,
      imageUrl: response.profileObj.imageUrl,
    });
  }

  function isSignedIn() {
    React.useEffect(() => {
      Socket.on('login-successful', (data) => {
        if (data.email === email && data.name === user) {
          console.log(data.name, data.email);
          props.setUsers(data.name);
          props.setEmail(data.email);
          props.setUrl(data.imageUrl);
          props.setLogin(true);
        }
      });
    });
  }

  const responseGoogle = (response) => {
    console.log(response);
  };

  isSignedIn();

  return (
    <GoogleLogin
      clientId="715626707407-s3aluro6ftbnbt5vd775gvi0p724amse.apps.googleusercontent.com"
      buttonText="Login with Google!"
      onSuccess={handleSubmit}
      onFailure={responseGoogle}
      cookiePolicy="single_host_origin"
    />
  );
}
