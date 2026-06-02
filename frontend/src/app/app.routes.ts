import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login';
import { DashboardComponent } from './components/dashboard/dashboard';
import { HomeComponent } from './components/dashboard/home/home';
import { ModelComponent } from './components/dashboard/model/model';
import { HistoryComponent } from './components/dashboard/history/history';
import { ProfileComponent } from './components/dashboard/profile/profile';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { 
    path: 'dashboard', 
    component: DashboardComponent, 
    canActivate: [authGuard],
    children: [
      { path: 'home', component: HomeComponent },
      { path: 'model', component: ModelComponent },
      { path: 'history', component: HistoryComponent },
      { path: 'profile', component: ProfileComponent },
      { path: '', redirectTo: 'home', pathMatch: 'full' }
    ]
  },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: '**', redirectTo: '/login' }
];
