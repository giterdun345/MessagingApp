import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools'

import Layout from './components/layout/LayoutPage'
import LoginPage from './components/login/LoginPage'
import RecievedList from './components/message_lists/RecievedList'
import SentList from './components/message_lists/SentList'
import ComposeMessage from './components/compose/ComposeMessage'
import MessageDetail from './components/details/MessageDetail'

import './App.css';
import 'antd/dist/antd.css';

const queryClient = new QueryClient()

const App = ()=> {
  return (
    <div className="App">
      <Router>  
        <Switch>
            <Route exact path='/' component={LoginPage} />
          <QueryClientProvider client={queryClient}>
            <Layout>
              <Route exact path='/inbox' component={RecievedList} />
              <Route exact path='/sent' component={SentList} />
              <Route exact path='/compose' component={ComposeMessage} />
              <Route exact path='/message/<:id>' component={MessageDetail} />
            </Layout>
            <ReactQueryDevtools initialIsOpen />
          </QueryClientProvider>
        </Switch>
      </Router>
      {/* login  */}
      {/* inbox */}
      {/* sentbox */}
      {/* compose  */}
      {/* message detail view  */}
    </div>
  );
}

export default App;
