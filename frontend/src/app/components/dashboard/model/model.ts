import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InfrahelpApiService } from '../../../services/infrahelp-api.service';

@Component({
  selector: 'app-model',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './model.html',
  styleUrl: './model.css'
})
export class ModelComponent implements OnInit {
  mlStatus: any = null;
  datasetSummary: any = null;
  loading = true;

  constructor(private apiService: InfrahelpApiService) {}

  ngOnInit() {
    this.apiService.getMlStatus().subscribe(res => {
      this.mlStatus = res;
      this.loading = false;
    });
    this.apiService.getDatasetSummary().subscribe(res => {
      this.datasetSummary = res;
    });
  }
}
