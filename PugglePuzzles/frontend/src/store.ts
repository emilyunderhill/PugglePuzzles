import { configureStore } from '@reduxjs/toolkit'
import { sudokusApi } from './features/sudokus/redux/sudokuApi'
import { setupListeners } from '@reduxjs/toolkit/query'
import { combineReducers } from "redux"
import { useDispatch, useSelector, type TypedUseSelectorHook } from 'react-redux'
import sudokuSlice, { name as sudokuSliceName} from './features/sudokus/redux/sudokuSlice'

const rootReducer = combineReducers({
    [sudokusApi.reducerPath]: sudokusApi.reducer,
    [sudokuSliceName]: sudokuSlice
  })


export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware({
        serializableCheck: false,
      }).concat(sudokusApi.middleware),
  devTools: process.env.NODE_ENV !== "production",

})

setupListeners(store.dispatch)

export type RootState = ReturnType<typeof rootReducer>
export type AppDispatch = typeof store.dispatch
export const useAppDispatch = useDispatch.withTypes<AppDispatch>()
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
