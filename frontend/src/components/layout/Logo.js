import { RadarChartOutlined } from '@ant-design/icons';

const Logo = () => {
  return ( 
    <div className='header-right'>
      <div className="logo-area">
        <RadarChartOutlined className='radar' style={{color:'white'}}/>
      </div>
      <h1 className='logo-title'>
        Project Message
      </h1>
    </div>
   );
}
 
export default Logo;