
import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/products')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch products')
        }
        return response.json()
      })
      .then((data) => {
        setProducts(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="container">
      <h1>Marketly</h1>
      <p>Welcome to Marketly Marketplace</p>

      <h2>Products</h2>

      {loading && <p>Loading products...</p>}

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div className="products">
        {products.map((product) => (
          <div className="product-card" key={product.id}>
            <h3>{product.title}</h3>
            <p>Price: {product.price.toLocaleString()} UZS</p>
            <p>Location: {product.location}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App
