<script setup lang="ts">
const stoptime: number = 100
const task = ref('');
const handleClick = async () => {
  const userMessage = task.value;
  const chatBody = document.querySelector('.chat-body');
  if (userMessage && chatBody) {

    const newUserMessage = createTypingMessage('あなた', userMessage, stoptime, false);
    chatBody.appendChild(newUserMessage);
    const content = await generateBotResponse(userMessage);
    console.log(content)
    const newAiMessage = createTypingMessage('AI', content, stoptime, true);
    chatBody.appendChild(newAiMessage);
    chatBody.scrollTop = chatBody.scrollHeight;
    task.value = '';
  }
};

function createTypingMessage(author:string, content:string, stoptime:number, isAnimationOff:boolean) {
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
    if (isAnimationOff) {
      const typingInterval = setInterval(() => {
        contentElement.textContent += content[index];
        index++;

        if (index === content.length) {
          clearInterval(typingInterval);
          messageElement.classList.add('active');
        }
      }, stoptime);
    } else {
      contentElement.textContent = content;
      messageElement.classList.add('active');
    }

    return messageElement;
  }

async function generateBotResponse(userMessage:string) {
  const { data: response } = await useFetch('/stage', {
        method: 'post',
        body: { "query": userMessage },
    });
  return response.value.answer
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
