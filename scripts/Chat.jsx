import React from 'react';
import Message from './Message';

export default function Chat(props) {
  return <Message message={props.messages} />;
}
