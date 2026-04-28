import { useCart } from "../context/CartContext";
import { Link } from "react-router-dom";

function CartPage() {
    const { cartItems,total, removeFromCart, updateQuantity } = useCart();
    const BASEURL = import.meta.env.VITE_DJANGO_BASE_URL;

    return (
        <div className="min-h-screen px-5 pb-10 pt-24 md:px-8">
            <h1 className="mb-6 text-center text-4xl font-bold text-stone-900">Your Shopping Bag</h1>
            {cartItems.length === 0 ? (
                <div className="mx-auto flex max-w-xl flex-col items-center rounded-2xl border border-dashed border-orange-200 bg-white/80 p-8 text-center text-stone-600">
                    <p>Your bag is empty right now. Add a few favorites and come back for checkout.</p>
                    <Link
                        to="/"
                        className="mt-5 rounded-xl bg-stone-900 px-6 py-3 text-sm font-semibold text-white transition hover:bg-black"
                    >
                        Back to Home
                    </Link>
                </div>
            ) : (
                <div className="mx-auto max-w-5xl rounded-3xl border border-orange-100 bg-white/90 p-6 shadow-lg md:p-8">
                    {cartItems.map((item) => (
                        <div
                            key={item.id}
                            className="mb-5 flex flex-col gap-4 rounded-2xl border border-orange-50 p-4 md:flex-row md:items-center md:justify-between"
                        >
                            <div className="flex items-center gap-4">
                                {item.product_image && (
                                    <img
                                        src={`${BASEURL}${item.product_image}`}
                                        alt={item.product_name}
                                        className="h-20 w-20 rounded-lg object-cover"
                                    />
                                )}
                            </div>
                            <div>
                                <h2 className="text-lg font-semibold text-stone-900">
                                    {item.product_name}
                                </h2>
                                <p className="text-stone-600">
                                    ${item.product_price}
                                </p>
                            </div>

                            <div className="flex items-center gap-3">
                                <button className="rounded-lg bg-orange-100 px-3 py-1 font-semibold text-orange-800"
                                    onClick={() =>
                                        updateQuantity(
                                            item.id,
                                            item.quantity - 1
                                        )
                                    }
                                >
                                    -
                                </button>
                                <span className="min-w-6 text-center font-semibold">{item.quantity}</span>
                                <button className="rounded-lg bg-orange-100 px-3 py-1 font-semibold text-orange-800"
                                    onClick={() =>
                                        updateQuantity(
                                            item.id,
                                            item.quantity + 1
                                        )
                                    }
                                >
                                    +
                                </button>
                                <button className="text-sm font-semibold text-red-600"
                                    onClick={() => removeFromCart(item.id)}
                                >
                                    Remove
                                </button>
                            </div>
                        </div>
                    ))}

                    <div className="mt-6 flex flex-col gap-4 border-t border-orange-100 pt-5 md:flex-row md:items-center md:justify-between">
                        <h2 className="text-xl font-bold text-stone-900">Total</h2>
                        <p className="text-2xl font-bold text-orange-700">${total.toFixed(2)}</p>
                        <Link to="/checkout" className="rounded-xl bg-stone-900 px-6 py-3 text-center text-sm font-semibold text-white transition hover:bg-black md:text-base">
                            Continue to checkout
                        </Link>
                    </div>
                </div>
            )}
        </div>
    )
}

export default CartPage;