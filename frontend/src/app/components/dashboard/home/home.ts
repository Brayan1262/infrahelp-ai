import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { InfrahelpApiService } from '../../../services/infrahelp-api.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class HomeComponent implements OnInit {
  ticketDescription = '';
  analysisResult: any = null;
  history: any[] = [];
  datasetSummary: any = null;
  mlStatus: any = null;
  categories: string[] = [];
  
  loading = false;
  errorMessage = '';

  constructor(private apiService: InfrahelpApiService) {}

  ngOnInit() {
    this.loadSystemData();
    this.loadHistory();
  }

  loadSystemData() {
    this.apiService.getMlStatus().subscribe({
      next: (res) => this.mlStatus = res,
      error: () => this.errorMessage = "No se pudo conectar con el backend."
    });
    
    this.apiService.getDatasetSummary().subscribe({
      next: (res) => this.datasetSummary = res,
      error: (err) => console.error(err)
    });
    
    this.apiService.getRecommendationCategories().subscribe({
      next: (res) => this.categories = res,
      error: (err) => console.error(err)
    });
  }

  loadHistory() {
    this.apiService.getHistory().subscribe({
      next: (res) => this.history = res,
      error: (err) => console.error(err)
    });
  }

  analyzeTicket() {
    if (!this.ticketDescription || this.ticketDescription.length < 10) {
      this.errorMessage = 'Ingrese una descripción mínima de 10 caracteres.';
      return;
    }
    this.errorMessage = '';
    this.loading = true;
    this.analysisResult = null;
    this.apiService.analyzeTicket(this.ticketDescription).subscribe({
      next: (res) => {
        this.analysisResult = res;
        this.loading = false;
        this.loadHistory();
      },
      error: (err) => {
        this.loading = false;
        this.errorMessage = 'No se pudo analizar el ticket. Intente nuevamente.';
      }
    });
  }

  getPriorityClass(priority: string): string {
    const p = priority?.toUpperCase();
    if (p === 'LOW') return 'bg-success';
    if (p === 'MEDIUM') return 'bg-warning text-dark';
    if (p === 'HIGH') return 'bg-orange';
    if (p === 'CRITICAL') return 'bg-danger';
    return 'bg-secondary';
  }

  getCategoryIcon(category: string): string {
    const c = category?.toUpperCase();
    if (c === 'REDES') return 'bi-router';
    if (c === 'WINDOWS_SERVER') return 'bi-windows';
    if (c === 'IMPRESORA') return 'bi-printer';
    if (c === 'SOFTWARE') return 'bi-window-stack';
    if (c === 'VIDEOVIGILANCIA') return 'bi-camera-video';
    if (c === 'BASE_DE_DATOS') return 'bi-database';
    if (c === 'SEGURIDAD') return 'bi-shield-lock';
    if (c === 'HARDWARE') return 'bi-pc-display';
    return 'bi-tag';
  }

  getTotalHistory(): number { return this.history.length; }

  getHistoryByCategory() {
    const counts: any = {};
    for (let t of this.history) {
      counts[t.predicted_category] = (counts[t.predicted_category] || 0) + 1;
    }
    return Object.keys(counts).map(key => ({
      name: key,
      count: counts[key],
      percentage: Math.round((counts[key] / (this.getTotalHistory()||1)) * 100)
    })).sort((a, b) => b.count - a.count);
  }

  getHistoryByPriority() {
    const counts: any = { 'LOW': 0, 'MEDIUM': 0, 'HIGH': 0, 'CRITICAL': 0 };
    for (let t of this.history) {
      if (counts[t.predicted_priority] !== undefined) counts[t.predicted_priority]++;
    }
    const total = this.getTotalHistory() || 1;
    return [
      { name: 'CRITICAL', count: counts['CRITICAL'], class: 'bg-danger', percentage: Math.round((counts['CRITICAL']/total)*100) },
      { name: 'HIGH', count: counts['HIGH'], class: 'bg-orange', percentage: Math.round((counts['HIGH']/total)*100) },
      { name: 'MEDIUM', count: counts['MEDIUM'], class: 'bg-warning', percentage: Math.round((counts['MEDIUM']/total)*100) },
      { name: 'LOW', count: counts['LOW'], class: 'bg-success', percentage: Math.round((counts['LOW']/total)*100) }
    ];
  }
}
