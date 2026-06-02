import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InfrahelpApiService {
  private baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  analyzeTicket(description: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/api/analyze`, { description });
  }

  getHistory(): Observable<any> {
    return this.http.get(`${this.baseUrl}/api/history`);
  }

  deleteHistory(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/api/history/${id}`);
  }

  getDatasetSummary(): Observable<any> {
    return this.http.get(`${this.baseUrl}/api/dataset/summary`);
  }

  getMlStatus(): Observable<any> {
    return this.http.get(`${this.baseUrl}/api/ml/status`);
  }

  getRecommendationCategories(): Observable<any> {
    return this.http.get(`${this.baseUrl}/api/recommendations/categories`);
  }

  askChatbot(message: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/api/chat/`, { message });
  }
}
