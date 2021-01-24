import { Component } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-app';
  table_values: any = [];
  choosenAuthor = '';
  choosenYear = '';
  sortPrice = '';
  authorNames: any = [];
  yearArray: any = [];
  priceArray: any = [];
  fileUploadName: any;
  constructor() {

  }
  ngOnInit() {
    this.getTableData();
  }

  sortingByAuthor(name: any) {
    this.choosenAuthor = name;
    this.getFilterData();
  }

  sortingByPrice(price: any) {
    axios.post('http://localhost:5000/sort', {
      price: this.table_values,
      field: price
    })
      .then((response) => {
        this.table_values = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
  }

  getFilterData() {
    axios.post('http://localhost:5000/filter', {
      author: this.choosenAuthor,
      year: this.choosenYear
    })
      .then((response) => {
        this.table_values = response.data;
        this.authorNames = [...new Set(response.data.map((item: { Author: any; }) => item.Author))];
        this.yearArray = [...new Set(response.data.map((item: { Year: any; }) => item.Year))];
      })
      .catch((error) => {
        console.log(error);
      })
  }

  sortingByYear(year: any) {
    this.choosenYear = year;
    this.getFilterData();
  }

  getTableData() {
    this.choosenAuthor = '';
    this.choosenYear = '';
    axios.get('http://localhost:5000/')
      .then((response) => {
        this.table_values = response.data
        this.authorNames = [...new Set(response.data.map((item: { Author: any; }) => item.Author))];
        this.yearArray = [...new Set(response.data.map((item: { Year: any; }) => item.Year))];
      })
      .catch((error) => {
        console.log(error);
      })
  }
}
