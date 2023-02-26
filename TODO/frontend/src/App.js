import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import axios from 'axios';
import Menu from './components/Menu.js';
import Footer from './components/Footers.js';


class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      'users': []
    };
  }

  componentDidMount() {
    // const users = [
    //   {
    //     'first_name': 'Фёдор',
    //     'last_name': 'Достоевский',
    //     'birthday_year': 1821
    //   },
    //   {
    //     'first_name': 'Александр',
    //     'last_name': 'Грин',
    //     'birthday_year': 1880
    //   },
    // ]
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        // const users = response.data
        this.setState(
          {
            'users': response.data.results
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <Menu/>
        <UserList users={this.state.users} />
        <Footer/>
      </div>
    );
  }
}

export default App;