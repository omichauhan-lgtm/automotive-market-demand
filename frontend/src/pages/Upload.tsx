import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function Upload() {
    const [file, setFile] = useState<File | null>(null)
    const [uploading, setUploading] = useState(false)
    const navigate = useNavigate()

    const handleUpload = async (e: React.FormEvent) => {
        e.preventDefault()
        if (!file) return

        const token = localStorage.getItem('token')
        const formData = new FormData()
        formData.append('file', file)

        setUploading(true)
        try {
            await axios.post('http://localhost:8000/ingest/upload-csv', formData, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
            alert('Upload Successful!')
            navigate('/dashboard')
        } catch (err) {
            alert('Upload Failed')
        } finally {
            setUploading(false)
        }
    }

    return (
        <div className="min-h-screen bg-gray-50 p-8 flex justify-center items-center">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-bold mb-6">Upload Dataset</h2>
                <form onSubmit={handleUpload}>
                    <div className="mb-6">
                        <label className="block text-gray-700 mb-2">Select CSV File</label>
                        <input
                            type="file"
                            accept=".csv"
                            onChange={e => setFile(e.target.files ? e.target.files[0] : null)}
                            className="w-full border p-2 rounded"
                        />
                    </div>
                    <button
                        disabled={uploading}
                        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
                    >
                        {uploading ? 'Uploading...' : 'Upload CSV'}
                    </button>
                </form>
                <button onClick={() => navigate('/dashboard')} className="mt-4 text-blue-600 w-full text-center">
                    Back to Dashboard
                </button>
            </div>
        </div>
    )
}
