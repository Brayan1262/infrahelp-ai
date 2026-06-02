import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.html',
  styleUrl: './profile.css'
})
export class ProfileComponent implements OnInit {
  profile = {
    name: 'Administrador',
    role: 'IT Support Engineer',
    avatar: 'https://ui-avatars.com/api/?name=Admin&background=0D8ABC&color=fff&size=128'
  };
  
  successMessage = '';

  ngOnInit() {
    const saved = localStorage.getItem('infrahelp_profile');
    if (saved) {
      this.profile = JSON.parse(saved);
    }
  }

  saveProfile() {
    localStorage.setItem('infrahelp_profile', JSON.stringify(this.profile));
    this.successMessage = 'Perfil guardado correctamente.';
    setTimeout(() => this.successMessage = '', 3000);
    window.dispatchEvent(new Event('profileUpdated'));
  }

  handleImageUpload(event: any) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.profile.avatar = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }
}
