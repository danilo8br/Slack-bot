## :rocket: Configurando o Webhook do Slack

Para enviar mensagens externas para o Slack, é necessario criar um aplicativo voltado para Webhooks.

## :grey_question: O que é um Webhook?

Webhook é uma forma de recebimento de informações, que são passadas quando um evento acontece. Dessa forma, o webhook na prática, é a forma de receber informações entre dois sistemas de uma forma passiva.

## :warning: Quais são os pré-requisitos?

Para criar um webhook no Slack, primeiramente tem que ter um workspace criado.

## Como configurar Webhook?


### Clique no menu do seu workspace, selecione "Administração" e depois "Gerenciar apps"

---

![Passo1](https://user-images.githubusercontent.com/51414398/165332255-5e35fb3b-a914-4179-a8c8-17b1f6abd02b.png)


### Em seguida, clique em "Desenvolver" no lado superior direito.

---


![Passo2](https://user-images.githubusercontent.com/51414398/165333253-5a221293-c171-4e28-ad0b-12b24cdd672d.PNG)


### Clique em "New App".

---

![Passo3](https://user-images.githubusercontent.com/51414398/165333574-457a860c-f076-4eb0-89b7-9d93bd2291b4.PNG)




### Selecione "From Scratch".

---

![Passo4](https://user-images.githubusercontent.com/51414398/165333781-e85e9f16-4f6b-449f-a4a9-9e487058b9ae.PNG)



### Escreva o nome do seu aplicativo, seleciona seu workspace e clique em "Create App".

---

![passo5](https://user-images.githubusercontent.com/51414398/165334073-2a2e77c9-7d29-4225-9b16-6431351b3810.PNG)


### Agora com o aplicativo criado, clique em "Incoming Webhooks" para configurar a URL.

---

![passo6](https://user-images.githubusercontent.com/51414398/165334589-98cd90de-60f8-4359-9042-d4006960fa8c.PNG)


### Clique no botão para ativar.

---

![passo7](https://user-images.githubusercontent.com/51414398/165334802-07d3760f-fb24-4a3e-85e4-09d3d19c0744.PNG)

---

### Finalizando, clique em "Add New Webhook to Workspace" para adicionar o canal e por fim, a URL.

---

![passo8](https://user-images.githubusercontent.com/51414398/165334987-771039de-6581-48fc-adb4-0440b46e1a6e.PNG)


### Agora só passar a URL para o código e enviar mensagens.

---

![PASSO9](https://user-images.githubusercontent.com/51414398/165335584-f473b8e7-a61a-44df-9257-51d801dc3fe5.PNG)


### Script Webhook

- [Script](Readme_Webhook/webhook_message.py/)