import { Component, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { InfrahelpApiService } from '../../../services/infrahelp-api.service';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.html',
  styleUrl: './chat.css'
})
export class ChatComponent {
  isOpen = false;
  messages: { text: string, sender: 'bot' | 'user' }[] = [];
  userInput = '';
  loading = false;

  @ViewChild('chatBody') private chatBody!: ElementRef;

  constructor(private apiService: InfrahelpApiService) {
    this.messages.push({
      text: '¡Hola! Soy InfraBot, tu asistente integrado. Pregúntame sobre el estado de los tickets, casos críticos o estadísticas del proyecto.',
      sender: 'bot'
    });
  }

  toggleChat() {
    this.isOpen = !this.isOpen;
    if (this.isOpen) {
      setTimeout(() => this.scrollToBottom(), 100);
    }
  }

  sendMessage() {
    if (!this.userInput.trim()) return;
    
    const msg = this.userInput;
    this.messages.push({ text: msg, sender: 'user' });
    this.userInput = '';
    this.loading = true;
    setTimeout(() => this.scrollToBottom(), 50);

    this.apiService.askChatbot(msg).subscribe({
      next: (res: any) => {
        this.messages.push({ text: res.reply, sender: 'bot' });
        this.loading = false;
        setTimeout(() => this.scrollToBottom(), 50);
      },
      error: () => {
        this.messages.push({ text: 'Hubo un error de conexión con mi sistema principal.', sender: 'bot' });
        this.loading = false;
        setTimeout(() => this.scrollToBottom(), 50);
      }
    });
  }

  scrollToBottom(): void {
    try {
      this.chatBody.nativeElement.scrollTop = this.chatBody.nativeElement.scrollHeight;
    } catch(err) { }
  }
}
