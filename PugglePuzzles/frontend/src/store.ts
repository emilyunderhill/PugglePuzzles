import { configureStore } from '@reduxjs/toolkit'
import { sudokusApi } from './features/sudokus/redux/sudokuApi'
import { setupListeners } from '@reduxjs/toolkit/query'
import { combineReducers } from "redux"
import { useDispatch } from 'react-redux'

const rootReducer = combineReducers({
    [sudokusApi.reducerPath]: sudokusApi.reducer
  })


export const store = configureStore({
  reducer: rootReducer,
    devTools: process.env.NODE_ENV !== "production",
})

setupListeners(store.dispatch)

export type RootState = ReturnType<typeof rootReducer>
export type AppDispatch = typeof store.dispatch
export const useAppDispatch = useDispatch.withTypes<AppDispatch>()
