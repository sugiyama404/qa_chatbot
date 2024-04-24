<script setup lang="ts">
const stoptime: number = 100
const task = ref('');
const handleClick = () => {
  const userMessage = task.value;
  const chatBody = document.querySelector('.chat-body');
  if (userMessage && chatBody) {

    const newUserMessage = createTypingMessage('あなた', userMessage, stoptime);
    chatBody.appendChild(newUserMessage);

    const sleeptime = userMessage.length * stoptime + 500
    setTimeout(() => {
      const content = generateBotResponse(userMessage)
      const newAiMessage = createTypingMessage('AI', content, stoptime);
      chatBody.appendChild(newAiMessage);
      chatBody.scrollTop = chatBody.scrollHeight;
      task.value = '';
    }, sleeptime);

  }
};

function createTypingMessage(author:string, content:string, stoptime:number) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', 'typeing');

    const authorElement = document.createElement('span');
    authorElement.classList.add('message-author');
    authorElement.textContent = author + ': ';
    messageElement.appendChild(authorElement);

    const contentElement = document.createElement('span');
    contentElement.classList.add('message-content');
    contentElement.textContent = '';
    messageElement.appendChild(contentElement);

    let index = 0;
    const typingInterval = setInterval(() => {
      contentElement.textContent += content[index];
      index++;

      if (index === content.length) {
        clearInterval(typingInterval);
        messageElement.classList.add('active');
      }
    }, stoptime);

    return messageElement;
  }

function generateBotResponse(userMessage:string) {
  console.log(userMessage);
  return "回答です。"
}

</script>
<template>
    <div class="chat-body">
      <div class="chat-message">
        <span class="message-author">あなた</span>
        <span class="message-content">こんにちは！</span>
      </div>
      <div class="chat-message">
        <span class="message-author">AI</span>
        <span class="message-content">こんにちは！何か質問はありますか？</span>
      </div>
    </div>
    <div class="chat-input">
      <input type="text" class="input-field" placeholder="質問を入力"  v-model="task">
      <button class="send-button" @click="handleClick">送信</button>
    </div>
</template>
