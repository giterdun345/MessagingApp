// import { useState } from 'react'
import { Layout } from 'antd';
import { useQuery } from 'react-query'
import NavLinks from './NavLinks'

const { Header, Content } = Layout

const LayoutPage = (props)=> {
  const {isLoading, isFetching, error, data, status } = useQuery("users_list", ()=>
    fetch('api/users')
    .then(res=> res.json())
  )

  console.log(data, status)
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <NavLinks users={data} isLoading={isLoading} isFetching={isFetching} error={error} status={status}/>
      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 0 }} />
          <Content style={{ margin: '0 16px' }}>
            {props.children}
          </Content>
      </Layout>
    </Layout>
  );
}


export default LayoutPage;