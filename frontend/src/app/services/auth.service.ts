import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedIn = false;

  constructor(private router: Router) {
    // Check session on load
    const savedSession = sessionStorage.getItem('infrahelp_admin_logged');
    if (savedSession === 'true') {
      this.isLoggedIn = true;
    }
  }

  login(user: string, pass: string): boolean {
    if (user === 'admin' && pass === 'admin') {
      this.isLoggedIn = true;
      sessionStorage.setItem('infrahelp_admin_logged', 'true');
      return true;
    }
    return false;
  }

  logout() {
    this.isLoggedIn = false;
    sessionStorage.removeItem('infrahelp_admin_logged');
    this.router.navigate(['/login']);
  }

  isAuthenticated(): boolean {
    return this.isLoggedIn;
  }
}
