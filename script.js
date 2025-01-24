const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbox");
const chatbottoggle = document.querySelector(".chatbot-toggle");

const createChatLi = (message, className) => {
    // Create a chat < list > element with passed meassage and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent =
        className === "outgoing"
            ? `<p></p>`
            : `<span class="material-symbols-outlined">💀</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi;
};

const handleChat = async () => {
    const userMessage = chatInput.value.trim();
    if (!userMessage) return;
    chatInput.value = "";

    // Append users chat meassage here in chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    const responseLi = createChatLi("Typing...", "incoming");
    chatbox.appendChild(responseLi);
    chatbox.scrollTo(0, chatbox.scrollHeight);

    // Send the message to the backend
    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
        });

        const data = await response.json();
        responseLi.querySelector("p").textContent = data.response;
    } catch (error) {
        responseLi.querySelector("p").textContent =
            "Something went wrong. Please try again.";
    }
};

sendChatBtn.addEventListener("click", handleChat);
chatbottoggle.addEventListener("click", () =>
    document.body.classList.toggle("show-chatbot")
);
