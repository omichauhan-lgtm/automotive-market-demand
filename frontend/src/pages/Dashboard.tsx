import { useEffect, useState } from 'react'
import axios from 'axios'
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts'
import { useNavigate } from 'react-router-dom'

export default function Dashboard() {
    const [kpis, setKpis] = useState<any>(null)
    const [segments, setSegments] = useState<any>(null)
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem('token')
        if (!token) {
            navigate('/login')
            return
        }

        const headers = { Authorization: `Bearer ${token}` }

        axios.get('http://localhost:8000/analytics/kpis', { headers })
            .then(res => setKpis(res.data))
            .catch(err => console.error(err))

        axios.get('http://localhost:8000/analytics/segments', { headers })
            .then(res => setSegments(res.data))
            .catch(err => console.error(err))
    }, [])

    if (!kpis) return <div className="p-8">Loading Dashboard...</div>

    const segmentData = segments ? Object.keys(segments.distribution).map(key => ({
        name: `Cluster ${key}`,
        count: segments.distribution[key]
    })) : []

    return (
        <div className="min-h-screen bg-gray-50 p-8">
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-3xl font-bold text-gray-800">AutoSight Dashboard</h1>
                <button onClick={() => navigate('/upload')} className="bg-green-600 text-white px-4 py-2 rounded">
                    Upload Data
                </button>
            </div>

            {/* KPIs */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Total Customers</h3>
                    <p className="text-2xl font-bold">{kpis.total_customers}</p>
                </div>
                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Avg Income</h3>
                    <p className="text-2xl font-bold">${kpis.avg_income.toLocaleString()}</p>
                </div>
                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Avg Purchase Prob</h3>
                    <p className="text-2xl font-bold">{(kpis.avg_purchase_prob * 100).toFixed(1)}%</p>
                </div>
                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500 text-sm">Top Region</h3>
                    <p className="text-2xl font-bold">{kpis.top_region}</p>
                </div>
            </div>

            {/* Charts */}
            <div className="bg-white p-6 rounded shadow mb-8">
                <h3 className="text-xl font-bold mb-4">Customer Segments Distribution</h3>
                <div className="h-64">
                    <ResponsiveContainer width="100%" height="100%">
                        <BarChart data={segmentData}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip />
                            <Bar dataKey="count" fill="#3b82f6" />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>
        </div>
    )
}
