import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InfrahelpApiService } from '../../../services/infrahelp-api.service';

@Component({
  selector: 'app-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './history.html',
  styleUrl: './history.css'
})
export class HistoryComponent implements OnInit {
  history: any[] = [];
  loading = true;

  constructor(private apiService: InfrahelpApiService) {}

  ngOnInit() {
    this.loadHistory();
  }

  loadHistory() {
    this.loading = true;
    this.apiService.getHistory().subscribe({
      next: (res) => { this.history = res; this.loading = false; },
      error: (err) => { console.error(err); this.loading = false; }
    });
  }

  deleteHistory(id: number) {
    if(confirm('¿Seguro que desea eliminar este ticket del historial?')) {
      this.apiService.deleteHistory(id).subscribe({
        next: () => this.loadHistory(),
        error: (err) => console.error(err)
      });
    }
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
    if (c === 'CORREO') return 'bi-envelope';
    if (c === 'SISTEMA_LENTO') return 'bi-speedometer2';
    return 'bi-tag';
  }
}
