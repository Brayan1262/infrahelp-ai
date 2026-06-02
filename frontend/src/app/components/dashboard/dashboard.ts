import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { ChatComponent } from './chat/chat';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule, ChatComponent],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class DashboardComponent implements OnInit, OnDestroy {
  profile = { name: 'Administrador', avatar: '' };
  private profileListener: any;

  constructor(private authService: AuthService, private router: Router) {}

  ngOnInit() {
    this.loadProfile();
    this.profileListener = () => this.loadProfile();
    window.addEventListener('profileUpdated', this.profileListener);
  }

  ngOnDestroy() {
    window.removeEventListener('profileUpdated', this.profileListener);
  }

  loadProfile() {
    const saved = localStorage.getItem('infrahelp_profile');
    if (saved) {
      const p = JSON.parse(saved);
      this.profile.name = p.name;
      this.profile.avatar = p.avatar || 'https://ui-avatars.com/api/?name=' + p.name + '&background=0D8ABC&color=fff';
    } else {
      this.profile.name = 'Administrador';
      this.profile.avatar = 'https://ui-avatars.com/api/?name=Admin&background=0D8ABC&color=fff';
    }
  }

  logout() {
    this.authService.logout();
  }
}
