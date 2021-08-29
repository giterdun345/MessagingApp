import { useState } from 'react'
import { Link } from 'react-router-dom'
import { Layout, Menu } from 'antd';
import { SendOutlined, FormOutlined, WechatOutlined, UserOutlined } from '@ant-design/icons';

import Logo from './Logo'

const { Sider } = Layout
const { SubMenu } = Menu

const NavLinks = ({ users, isLoading, isFetching, error, status }) => {
  const [collapsed, setCollapsed] = useState(false)

  const onCollapse = ()=> {
    setCollapsed(!collapsed)
  };

  return ( 
    <Sider collapsible collapsed={collapsed} onCollapse={onCollapse} >
      <Logo/>
      <Menu theme="dark" mode="inline">
        <Menu.Item key="1" icon={<WechatOutlined />}>
          <Link to='inbox'>
            Inbox
          </Link>
        </Menu.Item>
        <Menu.Item key="2" icon={<SendOutlined />}>
          <Link to='/sent'>
            Sent
          </Link>
        </Menu.Item>
        <Menu.Item key="3" icon={<FormOutlined />}>
          <Link to={{
                pathname:'/compose', 
                recipientProps:{
                  recipient: undefined
                }
              }}>
            Compose Message
          </Link>
        </Menu.Item>
        <SubMenu key="sub1" icon={<UserOutlined />} title="Users">
          {users.map((user, index) => {
            return(
              <Menu.Item key={`${user+index}`}>
                <Link to={{
                  pathname:'/compose', 
                  recipientProps:{
                    recipient: `${user.username}`
                  }
                }}>
                  {`${user.username}`}
                </Link>
              </Menu.Item>
            )     
          })}
        </SubMenu>
      </Menu>
    </Sider>
   );
}
 
export default NavLinks;