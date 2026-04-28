import {Link, useNavigate} from 'react-router-dom';
import {useCart} from '../context/CartContext.jsx';
import { clearTokens, getAccessToken } from '../utils/auth.js';

function Navbar() {
    const {cartItems} = useCart();
    const navigate = useNavigate();
    
    const cartCount = cartItems.reduce((total, item) => total + item.quantity, 0);
    
    const isLoggedIn = !!getAccessToken();

    const handleLogout = () => {
        clearTokens();
        navigate('/login');
    };
    return (
        <nav className='fixed top-0 z-50 w-full border-b border-white/40 bg-white/75 px-5 py-4 shadow-sm backdrop-blur-md md:px-8'>
            <div className='mx-auto flex w-full max-w-7xl items-center justify-between'>
            <Link to='/' className='text-lg font-bold tracking-tight text-stone-900 md:text-2xl'>
             Atelier Cart
            </Link>

            <div className='flex items-center gap-5 text-sm font-medium md:gap-8 md:text-base'>
                <Link to='/' className='text-stone-700 transition hover:text-orange-700'>
                    Home
                </Link>
                {/* Login/SignUp or Logout */}
                {!isLoggedIn ? (
                    <>
                        <Link to='/login' className='text-stone-700 transition hover:text-orange-700'>
                            Sign in
                        </Link>
                        <Link to='/signup' className='rounded-full bg-orange-100 px-4 py-2 text-orange-800 transition hover:bg-orange-200'>
                            Create account
                        </Link>
                    </>
                ) : (
                    <button onClick={handleLogout} className='text-stone-700 transition hover:text-orange-700'>
                        Logout
                    </button>
                )}
            </div>

            <Link to='/cart' className='relative rounded-full border border-orange-200 bg-white px-3 py-2 text-sm font-semibold text-stone-700 transition hover:border-orange-300 hover:text-orange-700 md:px-4'>
                Cart
                {cartCount > 0 && (
                    <span className='absolute -right-2 -top-2 rounded-full bg-orange-600 px-2 text-xs font-bold text-white'>
                        {cartCount}
                    </span>
                )}
            </Link>
            </div>
        </nav>
    )
}

export default Navbar;